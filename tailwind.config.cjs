/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'templates/*.html'
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem'

      }

    },
    extend: {
      colors: {
        primary: 'hsl(var(--color-primary) / <alpha-value>)',
        tertiary: 'hsl(var(--color-tertiary) / <alpha-value>)',
        black: 'hsl(var(--color-black) / <alpha-value>)',
        gray: 'hsl(var(--color-gray) / <alpha-value>)'
      }
    }
  },
  plugins: []
}
