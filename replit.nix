{pkgs}: {
  deps = [
    pkgs.ffmpeg-full
    pkgs.openssl
    pkgs.postgresql
    pkgs.docker
    pkgs.glibcLocales
  ];
}
