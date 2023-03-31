Name:		texlive-subdepth
Version:	15878
Release:	2
Summary:	Unify maths subscript height
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subdepth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is based on code (posted long ago to comp.text.tex
by Donald Arseneau) to equalise the height of subscripts in
maths. The default behaviour is to place subscripts slightly
lower when there is a superscript as well, but this can look
odd in some situations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subdepth/subdepth.sty
%doc %{_texmfdistdir}/doc/latex/subdepth/README
%doc %{_texmfdistdir}/doc/latex/subdepth/subdepth.pdf
#- source
%doc %{_texmfdistdir}/source/latex/subdepth/subdepth.dtx
%doc %{_texmfdistdir}/source/latex/subdepth/subdepth.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
