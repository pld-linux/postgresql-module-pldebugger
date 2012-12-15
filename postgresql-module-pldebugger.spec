Summary:	PL/pgSQL debugger server-side code
Summary(pl.UTF-8):	Debugger PL/pgSQL - kod działający po stronie serwera
Name:		postgresql-module-pldebugger
%define	snap	20121215
# version from pldbgapi.control - is it OK?
Version:	1.0
Release:	0.%{snap}.1
License:	Artistic
Group:		Applications/Databases
# git clone git://git.postgresql.org/git/pldebugger.git
# (master was equal to AS92_UPD-REL-9_2_2_4 tag)
Source0:	pldebugger.tar.xz
# Source0-md5:	4a3e881076df1844dc2d5c7f7dffbcc0
URL:		http://git.postgresql.org/gitweb/?p=pldebugger.git
BuildRequires:	postgresql-backend-devel >= 9.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a shared library which implements an API for debugging
PL/pgSQL functions on PostgreSQL 8.4 and above. The pgAdmin III
project (http://www.pgadmin.org/) provides a client user interface as
part of pgAdmin III v1.10.0 and above.

%description -l pl.UTF-8
Ten moduł to biblioteka współdzielona implementująca API dla funkcji
diagnostycznych PL/pgSQL serwera PostgreSQL w wersji 8.4 i nowszych.
Projekt pgAdmin III (http://www.pgadmin.org/) udostępnia interfejs
kliencki jako część pgAdmina III w wersji 1.10.0 i nowszych.

%prep
%setup -q -n pldebugger

%build
%{__make} \
	USE_PGXS=1 \
	CC="%{__cc}" \
	CUSTOM_COPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	USE_PGXS=1

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/postgresql

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.pldebugger
%attr(755,root,root) %{_libdir}/postgresql/plugin_debugger.so
%{_datadir}/postgresql/extension/pldbgapi--1.0.sql
%{_datadir}/postgresql/extension/pldbgapi--unpackaged--1.0.sql
%{_datadir}/postgresql/extension/pldbgapi.control
