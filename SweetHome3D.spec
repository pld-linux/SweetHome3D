# TODO
#$ SweetHome3D 
# Exception in thread "main" java.lang.NoClassDefFoundError: javax/jnlp/UnavailableServiceException
# Caused by: java.lang.ClassNotFoundException: javax.jnlp.UnavailableServiceException
# 	at java.net.URLClassLoader$1.run(URLClassLoader.java:202)
# 	at java.security.AccessController.doPrivileged(Native Method)
# 	at java.net.URLClassLoader.findClass(URLClassLoader.java:190)
# 	at java.lang.ClassLoader.loadClass(ClassLoader.java:307)
# 	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)
# 	at java.lang.ClassLoader.loadClass(ClassLoader.java:248)
# Could not find the main class: com.eteks.sweethome3d.SweetHome3D.  Program will exit.
Summary:	An interior design application
Name:		SweetHome3D
Version:	3.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/sweethome3d/%{name}-%{version}-linux-x86.tgz
# Source0-md5:	75d12e5972053ace7583a33c03afccc3
Source1:	http://downloads.sourceforge.net/sweethome3d/%{name}-%{version}-linux-x64.tgz
# Source1-md5:	21fbfcd53c71b2f730f4bba5f5082092
URL:		http://www.sweethome3d.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interior design application.

%prep
%ifarch %{ix86}
%setup -q -T -b0
%endif
%ifarch %{x8664}
%setup -q -T -b1
%endif

%{__sed} -i 's#exec "$PROGRAM_DIR"/jre1.6.0_22/bin/java#env java#g; 3,8 c\PROGRAM_DIR=%{_javadir}/SweetHome3D' SweetHome3D

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_javadir}/%{name}/lib
install lib/* $RPM_BUILD_ROOT%{_javadir}/%{name}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}
