import allure, pytest


class TestAllure:
    @allure.step("我是一个测试步骤")
    def test_001(self):
        # 对测试步骤进行描述  生成txt附件
        allure.attach("txt文件名字", "txt文件的内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_002(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_004(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_005(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_006(self):
        assert True



