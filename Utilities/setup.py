from distutils.core import setup,Extension

useful_dirs = [r'C:\Anaconda3\envs\analysis_general\Lib\site-packages\numpy\core\include\numpy',
               r'C:\Anaconda3\envs\analysis_general\Library\include\geos',
               r'C:\Anaconda3\envs\analysis_general\Library\include\geos\io\ByteOrderDataInStream.h']
module = Extension("Cmap",sources=['Cmap.c'],include_dirs=useful_dirs,requires=['Cython'],
    language='c++')
setup(name='Cmap',version='1.0',description='getcell',ext_modules=[module])
