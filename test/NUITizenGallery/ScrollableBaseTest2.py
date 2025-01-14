# test python script must be in same location as aurum_pb2.py

import grpc
from aurum_pb2 import *
from aurum_pb2_grpc import BootstrapStub
from NUIGalleryTestUtils import *
import time

isScrollableBase2PageOpened = False


# Check if notification test1 page is opened or not.
def CheckScrollableBase2TestStart(stub):
    LaunchAppTest(stub)

    global isScrollableBase2PageOpened
    isScrollableBase2PageOpened = FindTCByInputText(stub, "ScrollableBaseTest2")
    time.sleep(0.3)
    return isScrollableBase2PageOpened


# Check
def CheckScrollableBase21(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "ScrollTo" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))
            time.sleep(0.3)

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest21.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected21.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase22(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "ScrollToIndex" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest22.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected22.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase23(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "Remove" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest23.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected23.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase24(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "ReplaceLayout" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest24.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected24.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase25(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "SetScrollAvailableArea" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest25.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected25.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase26(stub):
    if not isScrollableBase2PageOpened:
        return False

    res = stub.findElements(ReqFindElements(widgetType='Button'))
    for elem in res.elements:
        if "RemoveAll" in elem.text:
            stub.click(ReqClick(type="ELEMENTID", elementId=elem.elementId))

            # Take screenshot
            screenShort = ReadScreenShotFile(stub, fileName="ScrollableBase/ScrollableBaseTest26.png")
            if screenShort is None:
                return False

            # Read image file expected
            expectedScreenShot = ReadImageFile(fileName='ScrollableBase/ScrollableBaseTestExpected26.png')
            if expectedScreenShot is None:
                return False

            # Check ssim
            return CheckSSIM(answerImge=expectedScreenShot, testTargetImage=screenShort)


def CheckScrollableBase2TestEnd(stub):
    global isScrollableBase2PageOpened
    isScrollableBase2PageOpened = False

    # Return to NUI Gallery page.
    stub.sendKey(ReqKey(type='XF86', actionType='STROKE', XF86keyCode='Return'))
    time.sleep(0.3)

    # Exit Gallery.
    stub.sendKey(ReqKey(type='XF86', actionType='STROKE', XF86keyCode='XF86Exit'))
    time.sleep(0.3)
    return True


def runTest(stub, testFunc):
    print("Testing started :", testFunc)
    result = testFunc(stub)
    print("Testing result :", result)
    return True


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = BootstrapStub(channel)
        runTest(stub, CheckScrollableBase2TestStart)
        runTest(stub, CheckScrollableBase21)
        runTest(stub, CheckScrollableBase22)
        runTest(stub, CheckScrollableBase23)
        runTest(stub, CheckScrollableBase24)
        runTest(stub, CheckScrollableBase25)
        runTest(stub, CheckScrollableBase26)
        runTest(stub, CheckScrollableBase2TestEnd)


if __name__ == '__main__':
    run()
