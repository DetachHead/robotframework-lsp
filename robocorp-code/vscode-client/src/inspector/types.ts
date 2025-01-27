/**
 * @source https://github.com/robocorp/inspector-ext/blob/master/src/utils/types.ts
 *! THIS FILE NEEDS TO ALWAYS MATCH THE SOURCE
 */

export declare enum LocatorType {
    Browser = "browser",
    Windows = "windows",
    Image = "image",
}

/**
 *
 * @export
 * @interface BrowserLocator
 */
export interface BrowserLocator {
    /**
     *
     * @type {DocType}
     * @memberof BrowserLocator
     */
    type: LocatorType.Browser;
    /**
     *
     * @type {string}
     * @memberof BrowserLocator
     */
    strategy: string;
    /**
     *
     * @type {string}
     * @memberof BrowserLocator
     */
    value: string;
    /**
     *
     * @type {string}
     * @memberof BrowserLocator
     */
    screenshot?: string;
    /**
     *
     * @type {string}
     * @memberof BrowserLocator
     */
    source?: string;
}
/**
 *
 * @export
 * @interface WindowsLocator
 */
export interface WindowsLocator {
    /**
     *
     * @type {LocatorType}
     * @memberof WindowsLocator
     */
    type: LocatorType.Windows;
    /**
     *
     * @type {string}
     * @memberof WindowsLocator
     */
    window: string;
    /**
     *
     * @type {string}
     * @memberof WindowsLocator
     */
    value: string;
    /**
     *
     * @type {number}
     * @memberof WindowsLocator
     */
    version: number;
    /**
     *
     * @type {string}
     * @memberof WindowsLocator
     */
    screenshot?: string;
}
/**
 *
 * @export
 * @interface ImageLocator
 */
export interface ImageLocator {
    /**
     *
     * @type {LocatorTypeAll}
     * @memberof ImageLocator
     */
    type: LocatorType.Image;
    /**
     *
     * @type {string}
     * @memberof ImageLocator
     */
    value: string;
    /**
     *
     * @type {string}
     * @memberof ImageLocator
     */
    path?: string;
    /**
     *
     * @type {number}
     * @memberof ImageLocator
     */
    confidence?: number;
    /**
     *
     * @type {string}
     * @memberof ImageLocator
     */
    screenshot?: string;
}

export declare type Locator = BrowserLocator | WindowsLocator | ImageLocator;
export declare type LocatorsMap = {
    [name: string]: Locator;
};
