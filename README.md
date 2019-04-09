# Djangoblog
<h2>Django Installation.</h2>
<p>Before we install Django we will get you to install an extremely useful tool to help keep your coding
environment tidy on your computer. <em>Virtual enviornment</em> will isolate your Python/Django setup on a per- project
 basis.</p>
 <p>All you need to do is find a directory in which you want to create the virtualenv; your home directory, for example. On 
 Windows, it might look like C:\Users\Name\ (where Name is the name of your login).</p>
 
 <p>For this tutorial we will be using a new directory djangogirls from your home directory:</p>

<p>command-line</p>
<p>$ mkdir djangoblog</p>
<p>$ cd djangoblog</p>

<h2> Installing Django </h2>
<p>Now that you have your virtualenv started, you can install Django.</p>
<p>Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:</p>

<p>command-line</p>
<p>$ python -m pip install --upgrade pip</p>

<h2>Error Installing on Windows</h2>
<p>If you get an error when calling pip on Windows platform, please check if your project pathname contains spaces, accents or special characters (for example, C:\Users\User Name\djangoblog). 
If it does, please consider using another place without spaces, accents or special characters (suggestion: C:\djangoblog). Create a new virtualenv in the new directory, then delete the old
one and try the above command again. (Moving the virtualenv directory won't work since virtualenv uses absolute paths.)</p>
