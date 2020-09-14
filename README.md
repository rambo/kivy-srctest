# srctest

Test Kivy with "src project structure"

Make a new virtualenv then

```
poetry install
kivysrctest
```

The above uses the setuptools entrypoint poetry creates

```
python main.py
```

Does the same thing but without going through the entrypoint.

I did this because elsewhere I was having weird issues where the setuptools entrypoint would not work but
using main.py would.
