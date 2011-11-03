# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/subdepth
# catalog-date 2008-08-23 22:26:13 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-subdepth
Version:	0.1
Release:	1
Summary:	Unify maths subscript height
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subdepth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdepth.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is based on code (posted long ago to comp.text.tex
by Donald Arseneau) to equalise the height of subscripts in
maths. The default behaviour is to place subscripts slightly
lower when there is a superscript as well, but this can look
odd in some situations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
