import pytest

CASE_TEMPLATE = """
*** Keywords ***
My Equal Redefined
    [Arguments]         ${arg1}     ${arg2}
    Should Be Equal     ${arg1}     ${arg2}

*** Task ***
Some task
    My Equal Redefined"""


@pytest.fixture
def check(workspace, libspec_manager, data_regression):
    def check_func(source, col_delta=0, expect_completions=True):
        from robotframework_ls.impl.completion_context import CompletionContext
        from robotframework_ls.impl import keyword_parameter_completions

        workspace.set_root("case2", libspec_manager=libspec_manager)
        doc = workspace.get_doc("case2.robot")
        doc.source = source

        line, col = doc.get_last_line_col()
        col += col_delta

        completions = keyword_parameter_completions.complete(
            CompletionContext(doc, workspace=workspace.ws, line=line, col=col)
        )

        if expect_completions:
            data_regression.check(completions)
        else:
            assert not completions

    return check_func


def test_keyword_completions_params_basic(check):
    check(CASE_TEMPLATE + "    ")


def test_keyword_completions_params_complete_existing(check):
    check(CASE_TEMPLATE + "    ar")


def test_keyword_completions_params_dont_complete(check):
    # in keyword name
    check(CASE_TEMPLATE + "", expect_completions=False)

    # in the middle of the parameter
    check(CASE_TEMPLATE + "    ar", col_delta=-1, expect_completions=False)

    # in the middle of the word
    check(CASE_TEMPLATE + "    ar", col_delta=-2, expect_completions=False)

    # in parameter assign part
    check(CASE_TEMPLATE + "    ar=", expect_completions=False)

    # in parameter assign part
    check(CASE_TEMPLATE + "    ar=a", expect_completions=False)
