/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html",  // Path to Flask templates
    "./static/js/**/*.js" //path to js files
  ],
  theme: {
    extend: {
        colors: {
          'black-bck':'rgba(2,6,23.0.45)',
        },
        keyframes: {
  
          marquee: {
            "0%": {
              transform: "translateY(100%)",
            },
            "100%": {
              transform: "translateY(-100%)",
            },
          },
        },
        animation: {
        
          marquee: "marquee 10s linear infinite",
          // Define the appear animation
        },
      },  
    
  },
  plugins: [
    require('tailwind-scrollbar'),
  ],
}

