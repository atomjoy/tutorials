# Scrollable Frame

Uruchom z python3 na Windows

## Instalacja

Zainstaluj pyton 3.12

```sh
# Install modules
phyton -m pip -m install tk
phyton -m pip -m customtkinter
phyton -m pip -m Pillow

# Upgrade
python -m pip install --upgrade SomePackage
python -m pip install --upgrade pip
```

## Style

Nie działa zmiana koloru tektu i anchora, trzeba zmienić przy tworzeniu objektu !!!

### Json

```json
{
    "CTkScrollableFrame": {
        "label_fg_color": ["#55cc55", "gray23"],
        "label_text_color": ["#fff", "gray23"],
        "label_anchor": ["w","w"]
    },
}
```

### Python class

```python
self.scrollable_label_button_frame = ScrollableLabelButtonFrame(
    master=self, width=300, command=self.label_button_frame_event, 
    corner_radius=5,
    label_text="Scrollable List Frame",    
    label_text_color=["#fff", "gray23"],
    label_anchor=["w", "w"],    
```

## Links

- <https://github.com/TomSchimansky/CustomTkinter>
- <https://customtkinter.tomschimansky.com/tutorial/scrollable-frames>
- <https://www.youtube.com/watch?v=Envp9yHb2Ho>
