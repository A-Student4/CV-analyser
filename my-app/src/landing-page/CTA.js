import { ArrowRight } from 'lucide-react';

export function Cta() {
  return (
    <section className="relative overflow-hidden bg-gradient-to-br from-sky-600 to-sky-700 px-6 py-24">
      <div className="mx-auto max-w-4xl text-center relative z-10">
        <h2 className="mb-6 text-4xl sm:text-5xl text-white">
          Ready to Launch Your Tech Career?
        </h2>
        <p className="mb-10 text-lg sm:text-xl text-sky-100">
          Join thousands of UK students who've successfully landed their dream tech roles with our platform.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-amber-400 to-amber-500 px-8 py-4 text-gray-900 shadow-lg hover:shadow-xl transition-all hover:scale-105">
            Start Free Trial
            <ArrowRight className="h-5 w-5" />
          </button>
          <button className="inline-flex items-center gap-2 rounded-full border-2 border-white px-8 py-4 text-white hover:bg-white/10 transition-colors">
            View Pricing
          </button>
        </div>
        
        <div className="mt-16 grid grid-cols-3 gap-8 border-t border-sky-500/30 pt-12">
          <div>
            <div className="mb-2 text-3xl sm:text-4xl text-amber-400">10k+</div>
            <div className="text-sm sm:text-base text-sky-200">Students Helped</div>
          </div>
          <div>
            <div className="mb-2 text-3xl sm:text-4xl text-amber-400">95%</div>
            <div className="text-sm sm:text-base text-sky-200">Success Rate</div>
          </div>
          <div>
            <div className="mb-2 text-3xl sm:text-4xl text-amber-400">500+</div>
            <div className="text-sm sm:text-base text-sky-200">Partner Companies</div>
          </div>
        </div>
      </div>
      
      {/* Decorative elements */}
      <div className="absolute top-0 right-0 -z-0 h-96 w-96 rounded-full bg-amber-400/10 blur-3xl" />
      <div className="absolute bottom-0 left-0 -z-0 h-96 w-96 rounded-full bg-sky-400/10 blur-3xl" />
    </section>
  );
}
