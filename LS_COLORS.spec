Name     : LS_COLORS
Version  : dfd04b75cf1f68400705fa01f76cd8144d7e9d39
Release  : 1
URL      : https://github.com/trapd00r/LS_COLORS/archive/%{version}.zip
Source0  : https://github.com/trapd00r/LS_COLORS/archive/%{version}.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl

%description
LS_COLORS
=========
This is a collection of extension:color mappings, suitable to use as your
LS COLORS environment variable. Most of them use the extended color map,
described in the ECMA-48 document; in other words, you'll need a terminal
with capabilities of displaying 256 colors.

%prep
%setup -q -n LS_COLORS-%{version}

%build

%install
mkdir -p %{buildroot}/usr/share/defaults/etc
install -m 0644 LS_COLORS %{buildroot}/usr/share/defaults/etc/

%files
%defattr(-,root,root,-)
/usr/share/defaults/etc/LS_COLORS
