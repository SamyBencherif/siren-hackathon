# siren-hackathon
Making sounds on a comp broh

## Dependencies

Audiogen does not work properly in Python3+, so we used Python2.7

### OSX
```
xcode-select --install
brew remove portaudio
brew install portaudio
pip install pyaudio
pip install audiogen
```

### Windows + Linux
```
pip install pyaudio
pip install audiogen
```

## Testing

To run tests run

```
python tests.py
```