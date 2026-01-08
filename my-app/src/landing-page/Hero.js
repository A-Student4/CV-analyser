import { ArrowRight } from 'lucide-react';
import { useNavigate } from 'react-router-dom';


export function Hero() {
  const navigate = useNavigate();

  return (
    <section className="relative overflow-hidden bg-gradient-to-br from-sky-50 to-white px-6 py-24 sm:py-32">
      <div className="mx-auto max-w-7xl">
        <div className="text-center">
          <h1 className="mb-6 text-5xl sm:text-6xl lg:text-7xl tracking-tight text-gray-900">
            Land Your Dream <br />
            <span className="bg-gradient-to-r from-sky-600 to-sky-400 bg-clip-text text-transparent">
              Tech Role
            </span>
          </h1>
          <p className="mx-auto mb-10 max-w-2xl text-lg sm:text-xl text-gray-600">
            Your complete toolkit for conquering tech applications. From CV perfection to acing 
            assessment centres, we've got UK tech students covered.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <button onClick={() => navigate('/app')} className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-amber-400 to-amber-500 px-8 py-4 text-gray-900 shadow-lg hover:shadow-xl transition-all hover:scale-105">
              Get Started
              <ArrowRight className="h-5 w-5" />
            </button>
            <button className="inline-flex items-center gap-2 rounded-full border-2 border-sky-300 px-8 py-4 text-sky-700 hover:bg-sky-50 transition-colors">
              Learn More
            </button>
          </div>
        </div>
      </div>
      
      {/* Decorative elements */}
      <div className="absolute top-0 right-0 -z-10 h-96 w-96 rounded-full bg-gradient-to-br from-sky-200/30 to-transparent blur-3xl" />
      <div className="absolute bottom-0 left-0 -z-10 h-96 w-96 rounded-full bg-gradient-to-tr from-amber-200/20 to-transparent blur-3xl" />
    </section>
  );
}
