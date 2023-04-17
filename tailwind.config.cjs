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
        'orange-base': 'hsl(var(--color-orange-base) / <alpha-value>)',
        'black-base': 'hsl(var(--color-black-base) / <alpha-value>)',
        'gray-base': 'hsl(var(--color-gray-base) / <alpha-value>)',
      },
    },

  },
  plugins: [],
}
