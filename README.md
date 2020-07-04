# Appium Tests

Example Appium tests that can be run on GenyMotion.

This repository contains:
* `ApiDemos-debug.apk` - Android application.
* `appium_test_1.py`, `appium_test_2.py` - Test cases.
* `requirements.txt` - List of required Python packages.
* `README.md` - This document.

## Setup
1. Install Appium.
2. Install Android Studio to have the ADB Connector.
3. Install Python requirements.
    ```
    $ pip3 install -r requirements.txt
    ```
4. Create a new account at https://www.genymotion.com/ and log in using `gmsaas` in the console.

## Running Test Cases
1. Start Android Studio.
2. Find a recipe eg: Google Pixel 2
    ```
    $ gmsaas recipes list | grep "Google Pixel 2"

    c52fdfc2-6914-4266-aa6e-50258f50ef91  Google Pixel 2           8.0        1080 x 1920 dpi 420  genymotion
    cbd25b62-a120-4ea2-9528-36f575478775  Google Pixel 2 XL        8.0        1440 x 2880 dpi 560  genymotion
    0203df5d-ee96-4930-be21-b55e9c445032  Google Pixel 2           8.1        1080 x 1920 dpi 420  genymotion
    c5b09eca-fd2f-4eb1-a6b5-4e7d9821e3e9  Google Pixel 2 XL        8.1        1440 x 2880 dpi 560  genymotion
    e6a305b5-ca40-4587-9aa8-623eb535b2f2  Google Pixel 2           9.0        1080 x 1920 dpi 420  genymotion
    dfbdd1bc-cce2-4f27-b8be-535b93ff9ee7  Google Pixel 2 XL        9.0        1440 x 2880 dpi 560  genymotion
    ```
Pick one, eg: `0203df5d-ee96-4930-be21-b55e9c445032`.

3. Start GenyMotion instance. It prints id of the new instance.
    ```
    $ gmsaas instances start 0203df5d-ee96-4930-be21-b55e9c445032 orzel

    d911ae81-2fff-4d01-ab5b-ee0c6fc5d8e6
    ```

4. Connect ADB.
    ```
    $ gmsaas instances adbconnect d911ae81-2fff-4d01-ab5b-ee0c6fc5d8e6
    ```

5. Check ADB connection.
    ```
    $ adb devices
    List of devices attached
    localhost:35939	device
    ```

6. Start Appium with host: `localhost`.
7. Run tests.
    ```
    $ python3 appium_test_1.py
    test_notifications (__main__.TestCaseOne) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 26.932s

    OK
    ```

    ```
    $ python3 appium_test_2.py

    test_wifi_settings (__main__.TestCaseTwo) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 38.496s

    OK
    ```
