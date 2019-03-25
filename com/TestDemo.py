
import lemoncheesecake.api as lcc

SUITE = {
    "description": "My Awesome Test Suite",
    "rank": 1
}


@lcc.test("My First Test")
def verifyMyFirstTest():
    lcc.log.info("Inside my first Test")

@lcc.test("My Second Test")
def verifyMySecondTest():
    lcc.log.info("Inside my first Test")

def teardown_suite():
        lcc.log_info("Do this after the suite...")
        print("Test")