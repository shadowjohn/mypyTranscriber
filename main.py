'''
   (C) 2019 Raryel C. Souza
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

#from pytranscriber.control.ctr_main import Ctr_Main
import multiprocessing
from pytranscriber.control.ctr_autosub import Ctr_Autosub
message = '''

Usage : main.exe [wavFile] [txtOutput]

'''

if __name__ == '__main__':
    multiprocessing.freeze_support()
    import sys
    #ctrMain = Ctr_Main()
    if len(sys.argv)!=3:
      print(message)
      sys.exit()
    sourceFile = sys.argv[1]
    outputFileSRT = sys.argv[2]
    langCode = "zh-TW" 
    fOutput = Ctr_Autosub.generate_subtitles(source_path = sourceFile,
                                    output = outputFileSRT,
                                    src_language = langCode,
                                    subtitle_file_format = 'raw',
                                    listener_progress = None) #self.listenerProgress)
    #sys.exit(main())
