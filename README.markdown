This is how I do it:

    mkproject testskel &&
    git init &&
    git pull git@github.com:jordanorelli/Django-Skeleton.git master &&
    rm README.markdown &&
    pip install -r requirements.txt &&
    ./manage.py syncdb &&
    ./manage.py runserver
