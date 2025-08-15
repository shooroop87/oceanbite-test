# Oceanbite Seafood — fishsite (Django 5)

Многостраничный сайт на Django Templates с интеграцией статических ассетов из HTML-архива.

## Структура
```
fishsite/
  manage.py
  requirements.txt
  fishsite/
    settings.py
    urls.py
    wsgi.py
  pages/
    templates/
      base.html
      partials/{header.html, footer.html, hero.html}
      home.html
      about.html
      species.html
      gallery.html
      contacts.html
      404.html
      500.html
    static/
      css/   ← из HTML-архива + chat.css
      js/    ← из HTML-архива + chat.js
      fonts/ ← из HTML-архива
      img/
        placeholders/{logo.svg, photo-16x9.jpg, photo-1x1.jpg}
```

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Статика и продакшн
```bash
python manage.py collectstatic
```
WhiteNoise уже включён (CompressedManifestStorage).

## Где править контент
- Логотип и изображения: `pages/static/img/placeholders/` (заменить файлы, пути уже подключены через `{% static %}`)
- Тексты: шаблоны в `pages/templates/` (home/about/species/gallery/contacts)
- Меню, логотип: `pages/templates/partials/header.html`
- Подвал: `pages/templates/partials/footer.html`
- Список карточек для `/species/` и `/gallery/` формируется во `pages/views.py` (статические данные).
- Контакты компании (адрес/почта/телефон): `pages/context_processors.py`
- Чат-кнопка: фронтенд без бэкенда (`static/js/chat.js`, `static/css/chat.css`) — открывает панель с ссылкой на email и форму.

## Примечания
- Макеты использованы для компоновки, стили и сетка — из HTML-архива (все css/js/fonts скопированы в `pages/static/`).
- Изображения — заглушки. Заменяйте на боевые через `pages/static/img/`.
- 404/500 оформлены в стиле сайта. Для проверки 404 можно открыть несуществующий URL. 500 отображается при `DEBUG=False`.
- Проект готов к дальнейшей интеграции каталога/корзины.
