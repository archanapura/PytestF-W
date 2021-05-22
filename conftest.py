import pytest
def pytest_addoption(parser):
    parser.addoption("--name",action="store")
    #parser.addoption("--appPack", action="store")


@pytest.fixture(scope="session")
def chrome_browser(request):
    print("hello ")
    #name_value = request.config.option.appPack
    v=request.config.getoption("--name")
    print(v)
    def teardown():
        print("bye bye!!!")

    request.addfinalizer(teardown)

