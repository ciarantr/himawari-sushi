/** @type {import("tailwindcss").Config} */
module.exports = {
  content: ['./templates/**/*.html', './static/src/js/**/*.ts'],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
      },
    },
    extend: {
      colors: {
        primary: 'hsl(var(--color-primary) / <alpha-value>)',
        tertiary: 'hsl(var(--color-tertiary) / <alpha-value>)',
        'black-base': 'hsl(var(--color-black-base) / <alpha-value>)',
        'gray-base': 'hsl(var(--color-gray-base) / <alpha-value>)',
      },
    },

  },
  plugins: [],
}
