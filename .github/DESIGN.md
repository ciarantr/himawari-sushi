# UX / UI 🎨

[Navigate back to README Documentation](./README.md)

My design process for the Himawari Sushi app began with the use of [Figma design tool](https://www.figma.com/). I
created designs for multiple
screen sizes, including mobile, iPad, and desktop, to ensure a seamless user experience across all devices.

To bring our design process to life, I conducted extensive research to choose the perfect colors and images for the
app. Looking at other successful restaurant apps and analyzed their use of color and imagery, as well as researched
the cultural significance of colors in Japanese cuisine.

To complement the imagery of the dishes available, I carefully selected a
color palette that would harmonize with the visual elements and create a cohesive and inviting experience for the users.
By taking the time to research and carefully choose our design elements, we were able to create an app that not only
looks beautiful, but also enhances the overall user experience.

## Colour Scheme

- `hsl(33, 100%, 57%)` used for headings, buttons, lists & hover underline effects.
- `hsl(344, 11%, 19%)` used for primary background & headings.
- `hsl(0, 1%, 40%)` used for paragraphs & secondary text.
- `hsl(0deg, 0%, 0%)` Tailwind predefined black throughout for backgrounds.

I used figma design tools to generate my colour palette.

![colour palette](../docs/design/colour-palette.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of
everywhere in the CSS file.

> **Note**
>
> Variables prefixed with `--color-` are used in tailwind config file to generate the tailwind colour palette & are not
> prefixed with hsl() values.
> See [Tailwindcss Using CSS variables](https://tailwindcss.com/docs/customizing-colors#using-css-variables) for more
> information.

```css
:root {
    --color-orange-base: 33 100% 57%;
    --color-black-base: 344 11% 19%;
    --color-gray-base: 0 1% 40%;
    --color-gray-shadow-base: hsl(0deg, 0%, 38%);
    --color-gray-shadow-dark: hsl(0deg, 0%, 34%);
    --color-gray-shadow-light: hsl(0deg, 0%, 42%);
}
```

🔝 [Back to Top](#ux--ui-)

## Typography

I refrained from using any custom fonts for this project, opting instead for the default fonts provided by the browser.
I deemed these fonts to be the most suitable for the project.

🔝 [Back to Top](#ux--ui-)

## Icons

I've used the [icons.js library](https://icones.js.org) to find suitable icons for my project. I've used the following
icons:

> **Note**
>
> The logo icon is no longer available, a suitable link is below and the original is available in
> the `docs/design/logo.svg`
> folder. The link below is a similar icon.

create a table like below: (use the table generator)

| Name                | Image                                                                                                    | URI                                                                          |
|---------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Logo                | ![logo](https://api.iconify.design/ic:sharp-ramen-dining.svg?color=%23FF9C24)                            | https://api.iconify.design/ic:sharp-ramen-dining.svg                         |
| Explore more        | ![explore more](https://api.iconify.design/mdi:arrow-right-bold-hexagon-outline.svg?color=%23FF9C24)     | https://api.iconify.design/mdi:arrow-right-bold-hexagon-outline.svg          |
| Book now            | ![book now](https://api.iconify.design/material-symbols:arrow-right-alt-rounded.svg?color=%23FF9C24)     | https://api.iconify.design/material-symbols:arrow-right-alt-rounded.svg      |
| Subscribe           | ![Subscribe](https://api.iconify.design/ion:paper-plane.svg?color=%23FF9C24)                             | https://api.iconify.design/ion:paper-plane.svg                               |
| Facebook            | ![facebook](https://api.iconify.design/ri:facebook-fill.svg?color=%23FF9C24)                             | https://api.iconify.design/ri:facebook-fill.svg                              |
| Instagram           | ![instagram](https://api.iconify.design/mdi:instagram.svg?color=%23FF9C24)                               | https://api.iconify.design/mdi:instagram.svg                                 |
| Twitter             | ![twitter](https://api.iconify.design/mdi:twitter.svg?color=%23FF9C24)                                   | https://api.iconify.design/mdi:twitter.svg                                   |
| Stripe              | ![Stripe](https://api.iconify.design/logos:stripe.svg)                                                   | https://api.iconify.design/logos:stripe.svg                                  |
| Visa                | ![visa](https://api.iconify.design/logos:visa.svg)                                                       | https://api.iconify.design/logos:visa.svg                                    |
| Paypal              | ![paypal](https://api.iconify.design/logos:paypal.svg)                                                   | https://api.iconify.design/logos:paypal.svg                                  |
| Profile             | ![profile](https://api.iconify.design/material-symbols:account-circle.svg?color=%23FF9C24)               | https://api.iconify.design/material-symbols:account-circle.svg               |
| Arrow down          | ![arrow down](https://api.iconify.design/ic:baseline-keyboard-arrow-down.svg?color=%23FF9C24)            | https://api.iconify.design/ic:baseline-keyboard-arrow-down.svg               |
| Log out             | ![log out](https://api.iconify.design/ic:twotone-logout.svg?color=%23FF9C24)                             | https://api.iconify.design/ic:twotone-logout.svg                             |
| Home                | ![home](https://api.iconify.design/clarity:house-solid.svg?color=%23FF9C24)                              | https://api.iconify.design/clarity:house-solid.svg                           |
| Booking             | ![booking](https://api.iconify.design/material-symbols:collections-bookmark-outline.svg?color=%23FF9C24) | https://api.iconify.design/material-symbols:collections-bookmark-outline.svg |
| Account information | ![account information](https://api.iconify.design/material-symbols:settings.svg?color=%23FF9C24)         | https://api.iconify.design/material-symbols:settings.svg                     |

🔝[Back To Top](#ux--ui-)