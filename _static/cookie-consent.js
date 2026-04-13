document.addEventListener("DOMContentLoaded", function () {
  // Already consented — nothing to show
  if (document.cookie.indexOf("qnd_cookie_consent=accepted") !== -1) return;

  // Detect language from <html lang="...">
  var lang = (document.documentElement.lang || "ja").toLowerCase();
  var isEn = lang.indexOf("en") === 0;

  var msg = isEn
    ? 'This site uses cookies (including Google Analytics) to improve your experience.'
    : 'このサイトではGoogle Analyticsなどの目的でCookieを使用しています。';
  var btnAccept = isEn ? 'Accept' : '同意する';
  var btnDecline = isEn ? 'Decline' : '拒否する';

  var banner = document.createElement("div");
  banner.id = "qnd-cookie-banner";
  banner.innerHTML =
    '<div class="qnd-cookie-inner">' +
      '<p class="qnd-cookie-msg">' + msg + '</p>' +
      '<div class="qnd-cookie-buttons">' +
        '<button id="qnd-cookie-accept" class="qnd-cookie-btn qnd-cookie-btn-accept">' + btnAccept + '</button>' +
        '<button id="qnd-cookie-decline" class="qnd-cookie-btn qnd-cookie-btn-decline">' + btnDecline + '</button>' +
      '</div>' +
    '</div>';
  document.body.appendChild(banner);

  function setCookie(value) {
    var expires = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toUTCString();
    var secure = location.protocol === "https:" ? "; Secure" : "";
    document.cookie = "qnd_cookie_consent=" + value + "; Path=/; Expires=" + expires + "; SameSite=Lax" + secure;
  }

  function closeBanner() {
    banner.style.transition = "opacity 0.3s ease";
    banner.style.opacity = "0";
    setTimeout(function () { banner.remove(); }, 300);
  }

  document.getElementById("qnd-cookie-accept").addEventListener("click", function () {
    setCookie("accepted");
    closeBanner();
    if (typeof qndLoadGA === "function") qndLoadGA();
  });

  document.getElementById("qnd-cookie-decline").addEventListener("click", function () {
    setCookie("declined");
    closeBanner();
  });
});
