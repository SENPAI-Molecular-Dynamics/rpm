Name:		senpai-strelitzia
Version:	1.0
Release:	1
Summary:	Manager for SENPAI worker nodes
License:	GPLv3
URL:		https://senpaimd.org
%undefine	_disable_source_fetch
Source0:	https://senpaimd.org/src/%{name}-%{version}-%{release}.tar.gz
Vendor:		SENPAI Molecular Dynamics
BuildArch:	x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gcc make

%description
Manager for SENPAI worker nodes

%prep
%setup -q -n STRELITZIA

%build
make

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/senpai
install -m 0755 strelitzia %{buildroot}/usr/bin/senpai-strelitzia
install -m 0644 strelitzia.conf %{buildroot}/etc/senpai/strelitzia.conf

%files
%attr(755,root,root) /usr/bin/senpai-strelitzia
%attr(644,senpai,senpai) /etc/senpai/strelitzia.conf

%changelog
* Thu May 05 2022 Sasha Emily Chelsea Murgia <mail@chelsea486mhz.fr> 1.0-1
- Initial RPM release
