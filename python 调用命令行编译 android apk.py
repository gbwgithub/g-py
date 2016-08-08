#!/usr/bin/env python
# -*- coding: utf-8 -*-


# python 调用命令行编译 android apk
 
# import os
# import subprocess
# import shutil
#
# def main():
#     sdk_path = os.getenv('ANDROID_HOME')
#     ndk_path = os.getenv('NDK_HOME')
#     standalone_path = os.getenv('NDK_STANDALONE')
#     directory = build_directory(sdk_path, args.output.filestem_str , native_shared_libs)
#
#     # // Copy the additional native libs into the libs directory.
#     for name, path in native_shared_libs.items():
#         shutil.copy( path,  os.path.join( directory, "libs/", "armeabi/",name)
#
#     # compile android_native_app_glue.c
#     cmd = os.path.join( standalone_path , "bin/" , "arm-linux-androideabi-gcc ")
#     arg1 = os.path.join( ndk_path, "sources/" , "android/" ,"native_app_glue/", "android_native_app_glue.c ")
#     arg2 = " -c "
#     arg3 = " -o "
#     arg4 = directory + "android_native_app_glue.o"
#
#     os.system(cmd + arg1 + arg2 + arg3 + arg4)
#
#     """
#     calling gcc to link a shared object
#     """
#     cmd = os.path.join(standalone_path , "bin/", "arm-linux-androideabi-gcc ")
#     arg1 = passthrough
#     arg2 = os.path.join( directory , "android_native_app_glue.o")
#     arg3 = " -o " + os.path.join( directory ,"libs", "armeabi", "libmain.so")
#     arg4 = " -shared"
#     arg5 = " -Wl,-E"
#     os.system(cmd + arg1 + arg2 + arg3 + arg4 + arg5 )
#
#     """
#     call ant debug
#     """
#
#     ant_command = "ant debug"
#     os.system(ant_command )
#
#     #copy apk file to required dest
#     shutil.copy( os.path.join( directory, "bin/", "rust-android-debug.apk"), output)
#
#
#
# def find_native_libs(args: &Args) -> HashMap<String, Path> {
#     """
#     args  HashMap
#     """
#     base_path = os.path.join( args, "native");
#     native_shared_libs = {}
#     #for dirpath, dirname, filenames in os.walk(base_path):
#
#     for dirs in os.listdir(base_path):
#         if os.path.isdir(dirs):
#             for dir in dirs:
#                 path = os.path.join(base_path, dirs,dir )
#                 for file in os.listdir(path):
#                     if file.starts_with("lib") and file.endwith(".so"):
#                         native_shared_libs.update(file, path)
#
#     return native_shared_libs
#
#
# def build_directory(sdk_dir, crate_name, libs):
#     """
#     sdk_dir : Path
#     crate_name : str
#     libs: HashMap<String, Path>
#
#     return: Tempdir
#
#     """
#     temp_dir = "android-rs-glue-rust-to-apk"
#     build_directory = os.mkdir( temp_dir )
#
#     if len(libs) > 0:
#         src_path = os.path.join(temp_dir ,"src/rust/glutin");
#         os.mkdirs(src_path )
#         java_file = open(os.path.join( src_path, "MainActivity.java") ,"rw")
#         java_file.write( (java_src(libs) )
#         activity_name = "rust.glutin.MainActivity"
#         java_file.flush()
#         java_file.close()
#     else:
#         activity_name = "android.app.NativeActivity"
#
#         manifest_file=os.path.join(build_directory, "AndroidManifest.xml")
#         manifest_file = open( manifest_file, "rw")
#         manifest_file.write(build_manifest(crate_name, activity_name))
#         manifest_file.close()
#
#         build_xml = os.path.join(build_directory, "build.xml")
#         build_xml = open( build.xml, "rw")
#         build_xml.write( build_build_xml() )
#         build_xml.close()
#
#         local_pro = os.path.join(build_directory, "local.properties")
#         local_pro  = open(local_pro, "rw")
#         local_pro.write(build_local_properties())
#         local_pro.close()
#
#         project_pro = os.path.join(build_directory, "project.properties")
#         project_pro = open(project_pro, "rw")
#         project_pro.write(build_project_properties())
#         project_pro.close()
#
#         libs_path = os.path.join(build_directory, "libs/", "armeabi")
#         os.makedirs(libs_path)
#
#         return build_directory
#
# def java_src(libs) {
#     """
#     libs: HashMap,
#     returns string
#     """
#     libs_string = ""
#
#     for  name, _ in libs.items():
#         """
#         // Strip off the 'lib' prefix and ".so" suffix. This is safe since libs only get added
#         // to the hash map if they start with lib.
#         """
#         line = "        System.loadLibrary(\"{}\");\n".format( name[3:len(name)-3]);
#         libs_string = libs_string + line;
#
#     ret = """package rust.glutin;
#
#     public class MainActivity extends android.app.NativeActivity {{
#         static {{
#             {0}
#         }}
#     }}""".format(libs_string)
#     return ret
#
#
#
# def  build_manifest(crate_name , activity_name):
#         return """<?xml version="1.0" encoding="utf-8"?>
# <!-- BEGIN_INCLUDE(manifest) -->
# <manifest xmlns:android="http://schemas.android.com/apk/res/android"
#         package="com.example.native_activity"
#         android:versionCode="1"
#         android:versionName="1.0">
#
#     <uses-sdk android:minSdkVersion="9" />
#
#     <uses-feature android:glEsVersion="0x00020000" android:required="true"></uses-feature>
#     <uses-permission android:name="android.permission.INTERNET" />
#     <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
#     <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
#
#     <application android:label="{0}">
#         <activity android:name="{1}"
#                 android:label="{0}"
#                 android:configChanges="orientation|keyboardHidden">
#             <intent-filter>
#                 <action android:name="android.intent.action.MAIN" />
#                 <category android:name="android.intent.category.LAUNCHER" />
#             </intent-filter>
#         </activity>
#     </application>
#
# </manifest>
# <!-- END_INCLUDE(manifest) -->
# """.format(crate_name, activity_name)
#
# def build_build_xml():
#         return """<?xml version="1.0" encoding="UTF-8"?>
# <project name="rust-android" default="help">
#     <property file="local.properties" />
#     <loadproperties srcFile="project.properties" />
#     <import file="custom_rules.xml" optional="true" />
#     <import file="${{sdk.dir}}/tools/ant/build.xml" />
# </project>
# """
#
#
# def build_local_properties(sdk_dir):
#     return "sdk.dir={0}".format(os.path.abspath(sdk_dir))
#
# def build_project_properties():
#     return "target=android-19"
#
# main()