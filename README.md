# Unit-тесты класса ```BooksCollector```

## Список тестов

### Метод ```add_new_book```

- ```test_add_new_book_add_two_books```:
  Проверка добавления книг

- ```test_add_new_book_add_existed_book_not_added```:
  Проверка добавления уже добавленной книги

- ```test_add_new_book_add_not_valid_len_book_name_not_added```:
  Проверки добавления книги с длиной названия более 40 символов и менее 1

### Метод ```set_book_genre```

- ```test_set_book_genre_set_exist_genre_for_exist_book_success```:
  Проверка назначения существующей книге существующего жанра

- ```test_set_book_genre_set_exist_genre_for_not_exist_book_fails```:
  Проверка назначения НЕ существующей книге существующего жанра

- ```test_set_book_genre_set_not_exist_genre_for_not_exist_book_fails```:
  Проверка назначения существующей книге НЕ существующего жанра

### Метод ```get_book_genre```

- ```test_get_book_genre_exist_book_success```:
  Проверка получения жанра существующей книги

- ```test_get_book_genre_not_exist_book_empty_response```:
  Проверка получения жанра НЕ существующей книги


### Метод ```get_books_with_specific_genre```

- ```test_get_books_with_specific_genre_exist_genre_success```:
  Проверка получения списка книг существующего жанра


- ```test_get_books_with_specific_genre_not_exist_genre_empty_list```:
  Проверка получения списка книг НЕ существующего жанра


- ```test_get_books_with_specific_genre_exist_genre_not_exist_book_empty_list```:
  Проверка получения пустого списка книг существующего жанра при отсутствии книг


### Метод ```get_books_for_children```

- ```test_get_books_for_children_success```:
  Проверка получения списка книг, подходящих детям


### Метод ```add_book_in_favorites```

- ```test_add_book_in_favorites_exist_book_success_added```:
  Проверка добавления существующей книги в избранное

- ```test_add_book_in_favorites_not_exist_book_not_added```:
  Проверка добавления не существующей книги в избранное

- ```test_add_book_in_favorites_already_added_book_not_added```:
  Проверка добавления уже добавленной книги в избранное


### Метод ```add_book_in_favorites```

- ```test_delete_book_from_favorites_added_book_success```:
  Проверка удаления из избранного добавленной ранее книги

- ```test_delete_book_from_favorites_not_added_book_not_delete```:
  Проверка удаления из избранного отсутствующей в избранном книги


### Метод ```get_books_genre```

Подкрывается тестами:
- ```test_add_new_book_add_two_books```
- ```test_add_new_book_add_existed_book_not_added```
- ```test_add_new_book_add_not_valid_len_book_name_not_added```




### Метод ```get_list_of_favorites_books```

Подкрывается тестами:
- ```test_add_book_in_favorites_exist_book_success_added```
- ```test_add_book_in_favorites_not_exist_book_not_added```
- ```test_add_book_in_favorites_already_added_book_not_added```
- ```test_delete_book_from_favorites_added_book_success```
- ```test_delete_book_from_favorites_not_added_book_not_delete```


## Итого тестами покрыты все методы класса ```BooksCollector```


