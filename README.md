# mypyTranscriber

Fork from pyTranscriber : https://github.com/raryelcostasouza/pyTranscriber 

pyTranscriber is an application that can be used to generate <b>automatic transcription / automatic subtitles </b> for audio/video files through a friendly graphical user interface. The hard work of speech recognition is made by the <a href="https://cloud.google.com/speech/">Google Speech Recognition API</a> using <a href="https://github.com/agermanidis/autosub">Autosub</a>.
<br>
<br>
![pyTranscriber1](doc/1.6.png?raw=true "pyTranscriber")
<br>
<br>
pyTranscriber is a improved version of my previous project <a href="https://github.com/raryelcostasouza/JAutosub">JAutosub (Java)</a>, created because of the limitations, issues, and overhead of mixing this 2 different languages on a single project.
<br>
<br>
The app by default outputs the subtitles as .srt and the transcribed audio on the user interface as well  as .txt files. SRT Files can be edited using <a href="http://www.aegisub.org/">Aegisub</a>.
Internet connection is REQUIRED because it uses the <a href="https://cloud.google.com/speech/">Google Cloud Speech Server</a> for the job, in the same way as the <a href="https://support.google.com/youtube/answer/6373554?hl=en">Youtube Automatic Subtitles</a>.
<br>
<br>
IMPORTANT: As speech recognition technology is still not fully accurate, the <b>accuracy</b> of the result can vary a lot, depending on many factors, mainly the <b>quality/clarity</b> of the audio. Ideally the audio input should not have background noise, sound effects or music. If there is a single speaker and he speaks in a clear and slow speed seems that the recognition is much more accurate. Sometimes, under ideal/lucky conditions it is possible to get a <a href="https://medium.com/@mlockrey/youtube-s-incredible-95-accuracy-rate-on-auto-generated-captions-b059924765d5">accuracy result close to 95%</a>.
<br>
<br>
Compiler 方法：<br>
<ul>
<li>c:\Python39-32\Scripts\pip install google-api-python-client</li>
<li>c:\Python39-32\Scripts\pip install requests</li>
<li>c:\Python39-32\Scripts\pip install progressbar</li>
<li>c:\Python39-32\Scripts\pip install pysrt</li>
<li>c:\Python39-32\Scripts\pip install pyinstaller</li>
詳見 build.bat<br>
</ul>
<br>
v1.6 使用方法：<br>
<br>
  main.exe [輸入的音檔] [輸出的文字檔] [音檔原語言] [輸出語言]
  語言列表 [zh-TW、zh-CN、en]
  
  目前只能繁轉簡、簡轉繁，無法中文轉英文，英文轉中文，又不是翻譯機...
  
  音檔原語言 預設為 zh-TW
  輸出語言 預設為 zh-TW
<br>
main.exe [wav Input] [txt Output] [wav lang=zh] [output Lang=zh-TW]<br>
<br>
例：<br>
<br>
cd dist<br>
main.exe test.wav test.txt
main.exe test.wav test.txt zh zh-TW<br>
main.exe test.wav test.txt zh zh-CN<br>
main.exe test.wav test.txt en en<br>
<br>    
<br>
<br>
<h1>Release Notes:</h1>
<b>09/06/2021 - v1.6: By 羽山 (https://3wa.tw)</b>
<br>* 增加載入音檔來源語言
<br>* 增加輸出語言，可簡、繁轉換
<br><br>
<b>26/10/2020 - v1.5: By 羽山 (https://3wa.tw)</b>
<br>* 改成 cli 執行
<br><br>
<b>29/01/2020 - v1.4:</b>
<br>* Fixed crash when exporting txt file for languages with special characters, specially chinese, on Windows system. Thanks for KY Poon for reporting!
<br><br>
<b>18/10/2019 - v1.3:</b>
<br>* Added option for not opening output transcription files automatically after finish
<br>* Fixed bug with canceling during batch processing (only the current job was being stopped... not all of them as expected).
<br><br>
<h1>For Users - Download the Windows/Linux/MacOS portable app</h1>
<a href="https://github.com/raryelcostasouza/pyTranscriber/releases/tag/v1.4-stable"> pyTranscriber-v1.4-stable</a>

<h1>For Developers - Technical Details</h1>
Check at <a href="https://github.com/raryelcostasouza/pyTranscriber/blob/master/doc/technical_details.md">technical_details.md<a>

<h1> Donations to support the development </h1>
pyTranscriber is developed as a hobby, so donations of any value are welcomed and essential for further improvements.
<br>If you feel that this software has been useful and would like to contribute for it to continue improve and have more features and fixes you can donate via Paypal to <b>raryel.costa@gmail.com</b> or bitcoin address <b>16rg9vG5aNpjgo7xXoVjRLJcjNYqxwtfEt</b>
<br>Thanks in advance!

### License

GPL v3
