document.addEventListener("DOMContentLoaded", function () {
  // 左サイドバー候補（テーマ差異を吸収するため複数用意）
  const selectors = [
    ".bd-sidebar .sidebar-primary-items", // pydata-sphinx-theme系(新)
    ".bd-sidebar .bd-links",              // pydata系のリンクコンテナ
    ".bd-sidebar-primary",                // 予備
    ".wy-menu-vertical",                  // sphinx_rtd_theme系(旧)
    ".wy-side-scroll",                    // 予備
    "nav[role='navigation']"              // 最終手段
  ];

  let parent = null;
  for (const sel of selectors) {
    const el = document.querySelector(sel);
    if (el) { parent = el; break; }
  }
  if (!parent) return;

  const box = document.createElement("div");
  box.className = "qns-contact";
  box.innerHTML = 'ワークショップや<br>企業向けサポートのご相談は <a href="https://qunasys.com/contact/" target="_blank" rel="noopener">QunaSys</a> までお気軽にどうぞ。';
  box.style.cssText =
    "margin:12px 8px 8px; padding:10px; border-top:1px solid #e5e7eb; text-align:center; font-size:0.9em;";
  parent.appendChild(box);
});
