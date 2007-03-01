Summary:	Serial line sniffer
#Summary(pl.UTF-8):	-
Name:		slsnif
Version:	0.4.4
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/slsnif/%{name}-%{version}.tar.gz
# Source0-md5:	78eeff8ba36ee0c3a954ec0878d2a997
URL:		http://www.sourceforge.net/projects/slsnif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serial line sniffer (slsnif). slsnif is a serial port logging utility.
It listens to the specified serial port and logs all data going
through this port in both directions.

#%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO slsnifrc-example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/slsnif.1*
