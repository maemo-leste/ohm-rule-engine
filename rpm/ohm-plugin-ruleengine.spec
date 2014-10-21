Name:       ohm-plugin-ruleengine

Summary:    A prolog-based OHM rule engine plugin
Version:    1.1.10
Release:    1
Group:      System/Resource Policy
License:    LGPLv2.1
URL:        https://github.com/nemomobile/ohm-rule-engine
Source0:    %{name}-%{version}.tar.gz
Requires:   swi-prolog-library-core
Requires:   ohm
Requires:   prolog-resourcepolicy-extensions
BuildRequires:  pkgconfig(libprolog) >= 1.1.10
BuildRequires:  pkgconfig(ohm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(swi-prolog)

%description
A prolog-based OHM rule engine plugin.


%package -n prolog-resourcepolicy-extensions
Summary:    Prolog extensions for the resource policy framework
Group:      System/Resource Policy
Requires:   %{name} = %{version}-%{release}

%description -n prolog-resourcepolicy-extensions
A set of prolog extensions needed by the resource policy framework
(and/or its prototype implementation).



%prep
%setup -q -n %{name}-%{version}


%build
%autogen --disable-static
%configure --disable-static \
    --enable-extra-warnings

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_libdir}/ohm/libohm_rule_engine.so
%config %{_sysconfdir}/ohm/plugins.d/rule_engine.ini

%files -n prolog-resourcepolicy-extensions
%defattr(-,root,root,-)
%dir %{_libdir}/prolog
%dir %{_libdir}/prolog/extensions
%{_libdir}/prolog/extensions/*