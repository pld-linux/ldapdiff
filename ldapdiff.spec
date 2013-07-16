Summary:	Tool for incremental LDAP directory updates based on ldif files
Name:		ldapdiff
Version:	1.4.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://launchpad.net/ldapdiff/trunk/%{version}/+download/%{name}-%{version}_src.tgz
# Source0-md5:	5da4ec7860cad79804d5af3958af7a2a
Patch0:		format-security.patch
URL:		http://launchpad.net/ldapdiff
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ldapdiff combines "diff" and "patch" functionality in one application.
The difference is, that ldapdiff is not designed for use on flat ascii
files, it is designed for "patching" ldap directories using ldif
files.

%prep
%setup -q
%patch0 -p1

# dirty tarball. cleanup
rm ldapdiff *.o

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	ldapdiffconfdir=%{_examplesdir}/%{name}-%{version} \
	ldapdiffsamplesdir=%{_examplesdir}/%{name}-%{version} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog debian/changelog TODO README
%attr(755,root,root) %{_bindir}/ldapdiff
%{_mandir}/man1/ldapdiff.1.*
%{_examplesdir}/%{name}-%{version}
