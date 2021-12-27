from robotframework_debug_adapter_tests.fixtures import _DebuggerAPI


def test_events_listener_basic(debugger_api: _DebuggerAPI):
    from robocorp_ls_core.debug_adapter_core.dap.dap_schema import (
        StartTestEvent,
        EndTestEvent,
        EndSuiteEvent,
        StartSuiteEvent,
        TerminatedEvent,
    )

    target = debugger_api.get_dap_case_file("case_evaluate.robot")
    debugger_api.target = target

    debugger_api.launch(
        target,
        debug=False,
        args=[
            "--listener=robotframework_debug_adapter.events_listener.EventsListenerV2"
        ],
    )

    debugger_api.configuration_done()

    start_suite_event = debugger_api.read(StartSuiteEvent).body
    assert start_suite_event.tests == ["Can use resource keywords"]
    assert debugger_api.read(StartTestEvent)
    assert debugger_api.read(EndTestEvent)
    assert debugger_api.read(EndSuiteEvent)
    debugger_api.read(TerminatedEvent)


def test_events_listener_failure(debugger_api: _DebuggerAPI):
    from robocorp_ls_core.debug_adapter_core.dap.dap_schema import (
        StartTestEvent,
        EndTestEvent,
        EndSuiteEvent,
        StartSuiteEvent,
        TerminatedEvent,
    )
    import robot

    target = debugger_api.get_dap_case_file("case_failure.robot")
    debugger_api.target = target

    debugger_api.launch(
        target,
        debug=False,
        args=[
            "--listener=robotframework_debug_adapter.events_listener.EventsListenerV2"
        ],
    )

    debugger_api.configuration_done()

    assert debugger_api.read(StartSuiteEvent)
    assert debugger_api.read(StartTestEvent)

    end_test_body = debugger_api.read(EndTestEvent).body
    assert end_test_body.status == "FAIL"
    if int(robot.get_version().split(".")[0]) >= 4:
        # source is not available on RF 3.
        assert len(end_test_body.failed_keywords) == 1
        assert end_test_body.failed_keywords[0]["lineno"] == 4

    assert debugger_api.read(EndSuiteEvent)

    debugger_api.read(TerminatedEvent)
