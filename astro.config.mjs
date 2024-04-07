import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

const algs = {
  label: "Algorithms",
  items: [
    {
      label: "Geometric Algorithms",
      items: [
        {
          label: "Introduction to Geometric Algorithms",
          link: "/algorithms/geometric/intro/",
        },
        {
          label: "Segment Intersection",
          link: "/algorithms/geometric/segment-intersection/",
        },
        {
          label: "Simple Polygons",
          link: "/algorithms/geometric/simple-polygons/",
        },
        {
          label: "Convex Hull",
          link: "/algorithms/geometric/convex-hull/",
        },
        {
          label: "Furthest Pair",
          link: "/algorithms/geometric/furthest-pair/",
        },
        {
          label: "Closest Pair",
          link: "/algorithms/geometric/closest-pair/",
        },
        {
          label: "Vertical and Horizontal Line Intersection",
          link: "/algorithms/geometric/vertical-horizontal-intersection/",
        },
      ],
    },
    {
      label: "Graph and Matching Algorithms",
      items: [
        {
          label: "Introduction to Matching Algorithms",
          link: "/algorithms/graphs-and-matching/intro/",
        },
        {
          label: "Bipartite Graph Matching",
          link: "/algorithms/graphs-and-matching/bipartite-matching/",
        },
        {
          label: "Network Flow",
          link: "/algorithms/graphs-and-matching/network-flow/",
        },
      ],
    },
  ],
};

const machineLearning = {
  label: "Machine Learning",
  items: [
    {
      label: "Regression",
      items: [
        // Each item here is one entry in the navigation menu.
        {
          label: "Intro to regression",
          link: "/machine-learning/regression/intro/",
        },
        {
          label: "Regression (sheet 1 recap)",
          link: "/machine-learning/regression/regression/",
        },
        {
          label: "Vectorised regression",
          link: "/machine-learning/regression/vectors/",
        },
        {
          label: "next one...",
          link: "/machine-learning/regression/regression/",
        },
        {
          label: "Worked Mathematics",
          items: [
            {
              label: "Analytical Solution for Optimised loss",
              link: "/machine-learning/regression/maths/optimal-loss",
            },
            {
              label:
                "Derivation: optimal parameters for vectorised linear regression",
              link: "/machine-learning/regression/maths/optimal-vectorised-loss",
            },
          ],
        },
      ],
    },
  ],
};

// https://astro.build/config
export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  integrations: [
    starlight({
      title: "My Docs",
      social: {
        github: "https://github.com/withastro/starlight",
      },
      head: [
        {
          tag: "link",
          attrs: {
            rel: "stylesheet",
            href: "https://cdn.jsdelivr.net/npm/katex@0.15.1/dist/katex.css",
            integrity:
              "sha384-WsHMgfkABRyG494OmuiNmkAOk8nhO1qE+Y6wns6v+EoNoTNxrWxYpl5ZYWFOLPCM",
            crossorigin: "anonymous",
          },
        },
      ],
      sidebar: [algs, machineLearning],
    }),
  ],
});
