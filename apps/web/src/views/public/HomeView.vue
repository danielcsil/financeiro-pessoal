<template>
    <main class="landing-page">

        <HeroSection />

        <AboutSection />

        <FeaturesSection />

        <DashboardPreview />

        <AiSection />

        <ModulesSection />

        <CTASection />

        <FooterSection />


    </main>
</template>

<script setup lang="ts">
  import HeroSection from "@/shared/components/landing/HeroSection.vue";
  import AboutSection from "@/shared/components/landing/AboutSection.vue";
  import FeaturesSection from "@/shared/components/landing/FeaturesSection.vue";
  import DashboardPreview from "@/shared/components/landing/DashboardPreview.vue";
  import AiSection from "@/shared/components/landing/AiSection.vue";
  import ModulesSection from "@/shared/components/landing/ModulesSection.vue";
  import CTASection from "@/shared/components/landing/CTASection.vue";
  import FooterSection from "@/shared/components/landing/FooterSection.vue";

  import "@/shared/styles/home.css";
</script>

<style scoped>

.landing-page{
    width:100%;
    min-height:100vh;
    background:var(--color-background);
}

</style>