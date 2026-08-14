from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru")

    cookie_user1 = {
        "name": "SESSION",
        "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
        "domain": "gitflic.ru"
    }

    cookie_user2 = {
        "name": "SESSION",
        "value": "OGNkMzgyZDQtODUyMC00MzFmLWFmMGMtY2MxYjVlMjQwMzVk",
        "domain": "gitflic.ru"
    }

    # Пользователь 1
    driver.add_cookie(cookie_user1)
    driver.refresh()

    driver.get("https://gitflic.ru/user/airsworld")
    url_user1 = driver.current_url

    # Выход
    driver.delete_all_cookies()
    driver.refresh()

    # Пользователь 2
    driver.add_cookie(cookie_user2)
    driver.refresh()

    driver.get("https://gitflic.ru/user/dravenqwq")
    url_user2 = driver.current_url

    print(url_user1)
    print(url_user2)
    assert url_user1 != url_user2

    driver.quit()