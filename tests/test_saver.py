from unittest.mock import patch


@patch("json.load")
def test_get_data(mock_load, test_saver):
    mock_load.return_value = ["a", "b", "c"]
    assert test_saver.get_data("a") == []


@patch("builtins.open")
@patch("json.load")
def test_get_data_1(mock_load, mock_open, test_saver):
    mock_open.return_value = mock_open()
    mock_load.return_value = ["a", "b", "c"]
    assert test_saver.get_data("a") == ["a", "b", "c"]


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_save_data(mock_dump, mock_open, mock_get, test_saver):
    mock_get.return_value = [
        {
            "id": "107370917",
            "name": "Онколог-хирург, маммолог",
            "alternate_url": "https://hh.ru/vacancy/107370917",
            "area": "Санкт-Петербург",
            "salary": {"from": 300000, "to": 500000, "currency": "RUR", "gross": True},
            "snippet": {
                "requirement": "Опыт работы в должности онколога-хирурга, <highlighttext>маммолога</highlighttext> "
                "не менее 6 лет. Наличие действующего сертификата специалиста. Умение работать в "
                "команде, ответственность...",
                "responsibility": "Проведение диагностики и лечения заболеваний молочной железы, включая "
                "онкологические заболевания. Выполнение хирургических операций различной "
                "сложности. Ведение амбулаторного приема пациентов. ",
            },
            "schedule": "Полный день",
        },
        {
            "id": "107642936",
            "name": "ВРАЧ ОНКОЛОГ",
            "alternate_url": "https://hh.ru/vacancy/107642936",
            "area": "Москва",
            "salary": {"from": 250000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": "высшее профильное образование. - наличие необходимых квалификационных сертификатов. "
                "- опыт работы с пациентами. - Опыт работы по специальности не менее 3-х лет. - ",
                "responsibility": "амбулаторный прием. - диагностика, лечение и профилактика заболеваний."
                "- консультирование по лабораторной диагностике. - проведение лечебных "
                "манипуляций. - ведение медицинской документации.",
            },
            "schedule": "Полный день",
        },
        {
            "id": "108123109",
            "name": "Инструктор ЛФК",
            "alternate_url": "https://hh.ru/vacancy/108123109",
            "area": "Кемерово",
            "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", '
                '"Лечебное дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть '
                "без опыта, но...",
                "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                "<highlighttext>маммология</highlighttext>, урология, гинекология). "
                "Работа на высокотехнологичном реабилитационном оборудовании. "
                "Обучение! Быть немного психологом и любить...",
            },
            "schedule": "Сменный график",
        },
    ]
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert (
        test_saver.save_data(
            {
                "id": "108123109",
                "name": "Инструктор ЛФК",
                "alternate_url": "https://hh.ru/vacancy/108123109",
                "area": "Кемерово",
                "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
                "snippet": {
                    "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", '
                    '"Лечебное дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть '
                    "без опыта, но...",
                    "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                    "<highlighttext>маммология</highlighttext>, урология, гинекология). "
                    "Работа на высокотехнологичном реабилитационном оборудовании. Обучение! "
                    "Быть немного психологом и любить...",
                },
                "schedule": "Сменный график",
            }
        )
        is None
    )


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_save_data_1(mock_dump, mock_open, mock_get, test_saver):
    mock_get.return_value = []
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert (
        test_saver.save_data(
            {
                "id": "108123109",
                "name": "Инструктор ЛФК",
                "alternate_url": "https://hh.ru/vacancy/108123109",
                "area": "Кемерово",
                "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
                "snippet": {
                    "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", '
                    '"Лечебное дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть '
                    "без опыта, но...",
                    "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                    "<highlighttext>маммология</highlighttext>, урология, гинекология). "
                    "Работа на высокотехнологичном реабилитационном оборудовании. Обучение! "
                    "Быть немного психологом и любить...",
                },
                "schedule": "Сменный график",
            }
        )
        is None
    )


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_save_dataset(mock_dump, mock_open, mock_get, vacancies_for_test, test_saver):
    mock_get.return_value = []
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert test_saver.save_dataset(vacancies_for_test) is None


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_save_dataset_1(mock_dump, mock_open, mock_get, vacancies_for_test, test_saver):
    mock_get.return_value = [
        {
            "id": "107370917",
            "name": "Онколог-хирург, маммолог",
            "alternate_url": "https://hh.ru/vacancy/107370917",
            "area": "Санкт-Петербург",
            "salary": {"from": 300000, "to": 500000, "currency": "RUR", "gross": True},
            "snippet": {
                "requirement": "Опыт работы в должности онколога-хирурга, <highlighttext>маммолога</highlighttext> "
                "не менее 6 лет. Наличие действующего сертификата специалиста. Умение работать в "
                "команде, ответственность...",
                "responsibility": "Проведение диагностики и лечения заболеваний молочной железы, включая "
                "онкологические заболевания. Выполнение хирургических операций различной сложности. "
                "Ведение амбулаторного приема пациентов. ",
            },
            "schedule": "Полный день",
        },
        {
            "id": "107642936",
            "name": "ВРАЧ ОНКОЛОГ",
            "alternate_url": "https://hh.ru/vacancy/107642936",
            "area": "Москва",
            "salary": {"from": 250000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": "высшее профильное образование. - наличие необходимых квалификационных сертификатов. "
                "- опыт работы с пациентами. - Опыт работы по специальности не менее 3-х лет. - ",
                "responsibility": "амбулаторный прием. - диагностика, лечение и профилактика заболеваний. - "
                "консультирование по лабораторной диагностике. - проведение лечебных манипуляций. "
                "- ведение медицинской документации.",
            },
            "schedule": "Полный день",
        },
        {
            "id": "108123109",
            "name": "Инструктор ЛФК",
            "alternate_url": "https://hh.ru/vacancy/108123109",
            "area": "Кемерово",
            "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", "Лечебное '
                'дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть без опыта, но...',
                "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                "<highlighttext>маммология</highlighttext>, урология, гинекология). Работа на "
                "высокотехнологичном реабилитационном оборудовании. Обучение! Быть немного "
                "психологом и любить...",
            },
            "schedule": "Сменный график",
        },
    ]
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert test_saver.save_dataset(vacancies_for_test) is None


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_delete_data(mock_dump, mock_open, mock_get, vacancies_for_test, test_saver):
    mock_get.return_value = [
        {
            "id": "107370917",
            "name": "Онколог-хирург, маммолог",
            "alternate_url": "https://hh.ru/vacancy/107370917",
            "area": "Санкт-Петербург",
            "salary": {"from": 300000, "to": 500000, "currency": "RUR", "gross": True},
            "snippet": {
                "requirement": "Опыт работы в должности онколога-хирурга, <highlighttext>маммолога</highlighttext> "
                "не менее 6 лет. Наличие действующего сертификата специалиста. Умение работать в "
                "команде, ответственность...",
                "responsibility": "Проведение диагностики и лечения заболеваний молочной железы, включая "
                "онкологические заболевания. Выполнение хирургических операций различной сложности. "
                "Ведение амбулаторного приема пациентов. ",
            },
            "schedule": "Полный день",
        },
        {
            "id": "107642936",
            "name": "ВРАЧ ОНКОЛОГ",
            "alternate_url": "https://hh.ru/vacancy/107642936",
            "area": "Москва",
            "salary": {"from": 250000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": "высшее профильное образование. - наличие необходимых квалификационных сертификатов."
                " - опыт работы с пациентами. - Опыт работы по специальности не менее 3-х лет. - ",
                "responsibility": "амбулаторный прием. - диагностика, лечение и профилактика заболеваний. - "
                "консультирование по лабораторной диагностике. - проведение лечебных манипуляций. "
                "- ведение медицинской документации.",
            },
            "schedule": "Полный день",
        },
        {
            "id": "108123109",
            "name": "Инструктор ЛФК",
            "alternate_url": "https://hh.ru/vacancy/108123109",
            "area": "Кемерово",
            "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", "Лечебное '
                'дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть без опыта, но...',
                "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                "<highlighttext>маммология</highlighttext>, урология, гинекология). Работа "
                "на высокотехнологичном реабилитационном оборудовании. Обучение! Быть немного "
                "психологом и любить...",
            },
            "schedule": "Сменный график",
        },
    ]
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert test_saver.delete_data("108123109") is None


@patch("src.saver.SaveDataInJsonFile.get_data")
@patch("builtins.open")
@patch("json.dump")
def test_delete_data_1(mock_dump, mock_open, mock_get, vacancies_for_test, test_saver):
    mock_get.return_value = [
        {
            "id": "107370917",
            "name": "Онколог-хирург, маммолог",
            "alternate_url": "https://hh.ru/vacancy/107370917",
            "area": "Санкт-Петербург",
            "salary": {"from": 300000, "to": 500000, "currency": "RUR", "gross": True},
            "snippet": {
                "requirement": "Опыт работы в должности онколога-хирурга, <highlighttext>маммолога</highlighttext> "
                "не менее 6 лет. Наличие действующего сертификата специалиста. Умение работать в "
                "команде, ответственность...",
                "responsibility": "Проведение диагностики и лечения заболеваний молочной железы, включая "
                "онкологические заболевания. Выполнение хирургических операций различной сложности. "
                "Ведение амбулаторного приема пациентов. ",
            },
            "schedule": "Полный день",
        },
        {
            "id": "107642936",
            "name": "ВРАЧ ОНКОЛОГ",
            "alternate_url": "https://hh.ru/vacancy/107642936",
            "area": "Москва",
            "salary": {"from": 250000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": "высшее профильное образование. - наличие необходимых квалификационных сертификатов. "
                "- опыт работы с пациентами. - Опыт работы по специальности не менее 3-х лет. - ",
                "responsibility": "амбулаторный прием. - диагностика, лечение и профилактика заболеваний. - "
                "консультирование по лабораторной диагностике. - проведение лечебных манипуляций. "
                "- ведение медицинской документации.",
            },
            "schedule": "Полный день",
        },
        {
            "id": "108123109",
            "name": "Инструктор ЛФК",
            "alternate_url": "https://hh.ru/vacancy/108123109",
            "area": "Кемерово",
            "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", '
                '"Лечебное дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть без '
                "опыта, но...",
                "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                "<highlighttext>маммология</highlighttext>, урология, гинекология). Работа на "
                "высокотехнологичном реабилитационном оборудовании. Обучение! Быть немного "
                "психологом и любить...",
            },
            "schedule": "Сменный график",
        },
    ]
    mock_open.return_value = mock_open()
    mock_dump.return_value = ""
    assert test_saver.delete_data("123") is None
