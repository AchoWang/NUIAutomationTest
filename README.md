# NUIAutomationTest
NUI Automation Test by Aurum. This test is designed to test NUITizenGallery examples. Test will take screenshots for each examples and compare with expected screenshots.

### Requirements and Pre-Conditions
- Aurum : Tizen UI Automator
  [Aurum Public](https://review.tizen.org/gerrit/#/admin/projects/platform/core/uifw/aurum) (Login Required)

- Tizen Device (Raspberry PI 4 Tizen)

- Device SDB Connection on PC

- sdb, python3 in PC

- Install latest packages on Device
  [NUITizenGallery](https://github.com/nui-dali/NUITizenGallery)
  [Tizen.NUI.WebViewTest](https://github.com/Samsung/TizenFX/tree/master/test/Tizen.NUI.WebViewTest) (Need to change csproj for binary build.)
  [Tizen.NUI.WidgetViewTest](https://github.com/Samsung/TizenFX/tree/master/test/Tizen.NUI.WidgetViewTest)

### Test Environment Settings
- Start from Aurum directory (aurum/)

  (host) cd ui_automation/python/mobile

  #### Create virtual env
  (host) python3 -m venv v

  #### Activate a virtual env
  Linux
  (host) source v/bin/activate
  Window
  (host) v/Scripts/activate.bat

  #### Install required pkg (only once)
  (python_virtual) pip3 install -r ../../../protocol/resources/python/requirements.txt

  #### Generate aurum.proto file for python (only once)
  (python_virtual) python3 -m grpc_tools.protoc --python_out=./ --grpc_python_out=./ -I ./../../../protocol/ ../../../protocol/aurum.proto

  #### Target setup such as sdb forward, bootstrap execution
  (python_virtual) python3 ../../../protocol/resources/python/mobile/mobileSetup.py

- Move test directory (NUIAutomationTest/)
  (host) cd test/NUITizenGallery/

  #### Take screenshots (only required first time)
  (host) python3 ScreenShotCapturer.py

  #### Run test
  (host) python3 {test-name}.py

  #### Run all test
  (host) python3 AllTest.py
