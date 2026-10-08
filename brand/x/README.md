# X (Twitter) banner: @meetLynkk

| File | Use |
|---|---|
| `x-banner-1500x500.png` | Standard X header size |
| `x-banner-3000x1000.png` | 2x version, sharper on retina screens (upload this one) |
| `x-banner-profile-preview.png` | Mockup of the banner on the profile page with the avatar |

Design: black background, headline "Your AI teammate for every meeting.", stage pills
(Before context, During live voice, After notes + tasks), "Start free at lynkk.ai", and a
large striped sphere echoing the Lynkk logo. The left ~420px is left empty because the
profile avatar covers the bottom-left of the header.

## Regenerate

`source/banner.html` is the editable design. Render it with Playwright:

```sh
NODE_PATH=$(npm root -g) node brand/x/source/render.js "$PWD/brand/x/source/banner.html" "$PWD/brand/x/x-banner-3000x1000.png" 2
```

The last argument is the scale (1 = 1500x500, 2 = 3000x1000).
