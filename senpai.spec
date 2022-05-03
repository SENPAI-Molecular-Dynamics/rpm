Name:		senpai
Version:	1.1
Release:	1
Summary:	Molecular dynamics simulator
License:	GPLv3
URL:		https://senpaimd.org
%undefine _disable_source_fetch
Source0:	https://senpaimd.org/src/%{name}-%{version}-%{release}.tar.gz
Vendor:		SENPAI Molecular Dynamics
BuildArch:	x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gcc
#Requires:	senpai-cm-int senpai-cm-frc senpai-cm-pot

%description
The SENPAI molecular dynamics (MD) simulator

%prep
%setup -q -n SENPAI

%build
make

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755  senpai %{buildroot}/usr/bin/senpai

%files
%attr(755,root,root) /usr/bin/senpai

%changelog
* Fri Apr 29 2022 Sasha Emily Chelsea Murgia <mail@chelsea486mhz.fr> 1.1-1
- Initial RPM release
