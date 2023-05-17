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
