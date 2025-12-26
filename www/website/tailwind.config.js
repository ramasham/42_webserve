/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./pages/**/*.{html,js}",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Primary - Deep Forest Confidence
        primary: {
          DEFAULT: "#2C5F41", // custom green-800
          50: "#E8F0EC",
          100: "#D1E1D9",
          200: "#A3C3B3",
          300: "#75A58D",
          400: "#478767",
          500: "#2C5F41",
          600: "#234C34",
          700: "#1A3927",
          800: "#12261A",
          900: "#09130D",
        },
        // Secondary - Mountain Meadow Warmth
        secondary: {
          DEFAULT: "#7BA05B", // custom green-500
          50: "#F2F6ED",
          100: "#E5EDDB",
          200: "#CBDBB7",
          300: "#B1C993",
          400: "#97B76F",
          500: "#7BA05B",
          600: "#628049",
          700: "#4A6037",
          800: "#314025",
          900: "#192012",
        },
        // Accent - Golden Hour Inspiration
        accent: {
          DEFAULT: "#D4AF37", // custom yellow-600
          50: "#FAF6E8",
          100: "#F5EDD1",
          200: "#EBDBA3",
          300: "#E1C975",
          400: "#D7B747",
          500: "#D4AF37",
          600: "#AA8C2C",
          700: "#7F6921",
          800: "#554616",
          900: "#2A230B",
        },
        // Background & Surface
        background: "#FAFBFC", // custom gray-50 - pristine snow
        surface: {
          DEFAULT: "#F5F7F8", // custom gray-100 - subtle cloud
          hover: "#EEF1F3",
        },
        border: "#E5E9EA", // form inputs and separation
        // Text Colors
        text: {
          primary: "#1A2B23", // custom gray-900 - mountain air clarity
          secondary: "#4A5D52", // custom gray-600 - gentle hierarchy
          tertiary: "#6B7F75",
        },
        // Semantic Colors
        success: {
          DEFAULT: "#5C8A3A", // custom green-600 - alpine growth
          light: "#E8F3E0",
        },
        warning: {
          DEFAULT: "#B8860B", // custom yellow-700 - careful attention
          light: "#FDF6E3",
        },
        error: {
          DEFAULT: "#8B4513", // custom orange-800 - warm concern
          light: "#FDF0E8",
        },
      },
      fontFamily: {
        headline: ['"Crimson Text"', 'serif'], // Headlines - sophisticated editorial
        body: ['"Source Sans 3"', 'sans-serif'], // Body - clean Swiss precision
        cta: ['Montserrat', 'sans-serif'], // CTAs - confident action clarity
        accent: ['"Playfair Display"', 'serif'], // Accents - elegant moments
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.75rem' }],
        'lg': ['1.125rem', { lineHeight: '1.875rem' }],
        'xl': ['1.25rem', { lineHeight: '2rem' }],
        '2xl': ['1.5rem', { lineHeight: '2.25rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.5rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.75rem' }],
        '5xl': ['3rem', { lineHeight: '3.5rem' }],
        '6xl': ['3.75rem', { lineHeight: '4rem' }],
        '7xl': ['4.5rem', { lineHeight: '4.75rem' }],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '100': '25rem',
        '112': '28rem',
        '128': '32rem',
      },
      borderRadius: {
        'lg': '0.5rem',
        'xl': '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
      },
      transitionDuration: {
        '300': '300ms',
        '450': '450ms',
        '600': '600ms',
      },
      transitionTimingFunction: {
        'ease-out': 'cubic-bezier(0, 0, 0.2, 1)',
      },
      animation: {
        'fade-in': 'fadeIn 600ms ease-out forwards',
        'slide-up': 'slideUp 600ms ease-out forwards',
        'scale-in': 'scaleIn 450ms ease-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(40px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
      },
      boxShadow: {
        'focus': '0 0 0 3px rgba(44, 95, 65, 0.3)',
      },
      aspectRatio: {
        'hero': '16 / 9',
        'card': '4 / 3',
        'portrait': '3 / 4',
      },
      backdropBlur: {
        xs: '2px',
      },
      maxWidth: {
        '8xl': '88rem',
        '9xl': '96rem',
      },
    },
  },
  plugins: [],
}