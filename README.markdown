This is how I do it:

    mkproject --no-site-packages --prompt=testskel: -p python2.7 testskel &&
    git init &&
    git pull git@github.com:jordanorelli/Django-Skeleton.git master &&
    rm README.markdown &&
    pip install -r requirements.txt &&
    ./manage.py syncdb &&
    ./manage.py runserver
