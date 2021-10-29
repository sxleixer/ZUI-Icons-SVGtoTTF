# Setup

* Install Python 3: I am using `Python 3.8.6`
* Install [FontForge](https://fontforge.org/en-US/): Iam using version `FontForge-2020-11-07-Windows.exe`
* Clone `zui-icons` repository: `git clone https://github.com/ZEISS/zui-icons.git <FolderName>/zui-icons`
* Clone `svgs2ttf` repository: `git clone https://github.com/pteromys/svgs2ttf.git <FolderName>/svgs2ttf`
* Clone `ZUI-Icons-SVGtoTTF` repository: `git clone https://github.com/sxleixer/ZUI-Icons-SVGtoTTF.git <FolderName>/ConvertZUIIconsToTTF`
* Change into the `<FolderName>/ConvertZUIIconsToTTF` directory


# Usage

* Execute `convert.ps1` which will ultimately create a `config.json` like and a `ZUiUcons.ttf` file:
```json
{
 "props": {
  "ascent": 200,
  "descent": 200,
  "em": 1000,
  "family": "ZUiIcons"
 },
 "input": "C:/Workspace/zui-icons/src",
 "output": [
  "ZUiIcons.ttf"
 ],
 "glyphs": {
  "0x41": "alerts-communications/alert_status_circle_32.svg",
  [...]
  "0x31d": "workbench/zen_connect_video_renderer_24.svg"
 }
}
```


# Issues
* Every SVG will be traversed in a possibly ambiguous order.
* When new SVGs are added the following glyphs will be shifted by the amount of SVGs added in between

