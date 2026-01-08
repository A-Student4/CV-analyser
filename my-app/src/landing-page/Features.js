import { FileText, Target, UserCheck, Building2 } from 'lucide-react';


const features = [
  {
    icon: FileText,
    title: 'CV Analysis',
    description: 'Get expert feedback on your CV with AI-powered insights tailored for UK tech roles.',
    color: 'from-sky-400 to-sky-500',
  },
  {
    icon: Target,
    title: 'Online Tests',
    description: 'Practice aptitude tests, coding challenges, and technical assessments with real examples.',
    color: 'from-amber-400 to-amber-500',
  },
  {
    icon: UserCheck,
    title: 'Interview Prep',
    description: 'Master behavioral and technical interviews with guided practice and feedback.',
    color: 'from-sky-500 to-sky-600',
  },
  {
    icon: Building2,
    title: 'Assessment Centres',
    description: 'Prepare for group exercises, presentations, and case studies with confidence.',
    color: 'from-amber-500 to-amber-600',
  },
];

export function Features() {
  return (
    <section className="px-6 py-24 bg-white">
      <div className="mx-auto max-w-7xl">
        <div className="text-center mb-16">
          <h2 className="mb-4 text-4xl sm:text-5xl text-gray-900">
            Everything You Need to Succeed
          </h2>
          <p className="mx-auto max-w-2xl text-lg text-gray-600">
            Comprehensive support at every stage of your tech application journey
          </p>
        </div>
        
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature, index) => (
            <div
              key={index}
              className="group relative overflow-hidden rounded-3xl border border-gray-100 bg-white p-8 shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
            >
              <div className={`mb-6 inline-flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br ${feature.color} shadow-lg`}>
                <feature.icon className="h-7 w-7 text-white" />
              </div>
              <h3 className="mb-3 text-xl text-gray-900">
                {feature.title}
              </h3>
              <p className="text-gray-600">
                {feature.description}
              </p>
              
              {/* Decorative gradient on hover */}
              <div className={`absolute inset-0 -z-10 bg-gradient-to-br ${feature.color} opacity-0 group-hover:opacity-5 transition-opacity`} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
