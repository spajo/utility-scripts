# Utility scripts which I wrote lol

## clipboard.py

This script strips the copied string of newlines.

## icons.py

This scripts converts css icons such as

```css
.icon-alarm-level1::before {  
    content: '\e902';
}
```

to public static fields with javadocs in java as such (it probably won't be rendered here because of missing fonts lol)

```java
/**
 * <span style="font-size: 80px;" ></span>
 */
public static final String ALARM_LEVEL1 = "\ue902";
```

## Authors

* **Rafal Janicki** - *this project* - [spajo](https://github.com/spajo)

## License

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2018 Rafal Janicki <janicki@spaj.eu>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.