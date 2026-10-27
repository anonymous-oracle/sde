# Part 30 · Supplementary Applied Domains: Corporate Finance, Marketing, Learning Analytics & Game Engines · TOPIC LIST

Rules and directives for this part: `index/part30_supplementary_applied_domains.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Supplementary Applied Domains: Corporate Finance, Marketing, Learning Analytics & Game Engines

### Corporate finance

- **Goals and governance**: profit versus shareholder-wealth maximization; the agency problem; corporate governance; sources of finance (equity, debt, hybrids, retained earnings)
- **Time value of money**: compounding and discounting; annuities and perpetuities; the effective annual rate; valuing bonds (yield to maturity) and stocks (dividend discount, Gordon growth)
- **Capital budgeting**: incremental cash flows, sunk and opportunity costs, depreciation tax shields, working capital; NPV, IRR (and multiple IRRs), MIRR, payback and discounted payback, profitability index; ranking conflicts and capital rationing; sensitivity and scenario analysis
- **Return, risk and portfolio theory**: expected return and variance; correlation and diversification; the efficient frontier; CAPM, beta and the security market line
- **Cost of capital**: costs of debt, preferred and equity; WACC and firm value
- **Leverage and capital structure**: operating, financial and combined leverage; EBIT–EPS analysis; Modigliani–Miller with and without taxes, trade-off theory, pecking order
- **Working capital**: liquidity measures; operating and cash-conversion cycles; inventory control (EOQ, reorder point); receivables and credit policy; cash management
- **Dividend decisions**: Gordon, Walter and Modigliani–Miller irrelevance; Lintner's smoothing; buybacks and signalling

### Marketing and digital marketing

- **Marketing fundamentals**: eras of marketing; branding; segmentation, targeting and positioning; the 4Ps, 3Ps for services and 4Cs
- **Digital marketing**: the RACE and AIDA frameworks; the channel ecosystem; performance metrics (impressions, click-through rate, conversion, cost per acquisition, return on ad spend)
- **Content marketing**: content types; the funnel (top, middle and bottom) and matching content to stage; AI in the content workflow
- **Social media, influencer marketing and SEO**: platform strategy and a social media plan; influencer selection and measurement; search-engine optimization (on-page, off-page, technical)
- **Email marketing**: list building, segmentation, campaigns and deliverability; AI-powered campaigns

### Learning analytics

- **Foundations**: learning analytics versus academic analytics and educational data mining; the four levels (descriptive, diagnostic, predictive, prescriptive)
- **Data and ethics**: educational data sources (LMS logs, assessments, forums); technology-enhanced learning; ethics and student privacy
- **Descriptive analytics**: chart choice and comparison; dashboards; spreadsheet analysis
- **Sequence and process analysis**: sequential pattern mining; differential sequence mining; process mining
- **Multimodal learning analytics**: affective computing and eye tracking as signals of engagement
- **Tools**: Weka, Orange, iSAT, ProM and Excel

### Game engines and real-time rendering

- **Game loop and engine runtime architecture**: the loop of input, update and render once per frame; engine subsystems (resources, world, renderer, physics, audio, scripting) and their startup and shutdown order; a fixed simulation step decoupled from a variable render rate
- **Entity-component object models**: entities as identifiers, components as plain data and systems as functions over sets of components; composition in place of deep inheritance; components packed in dense arrays for cache-friendly iteration; the trade-off against object hierarchies in gameplay code
- **Memory management for engines**: per-frame linear (bump) allocators reset each frame, pool allocators for fixed-size objects and stack allocators for scoped work; fragmentation and the cost of general-purpose allocation inside the frame loop; the frame budget as the constraint that makes allocation-free paths necessary
- **Skeletal animation**: a rig of joints in a hierarchy, each with a local transform; skinning vertices by weighted sums of joint matrices (linear blend skinning); keyframe interpolation with quaternion slerp for rotations; blending and state machines over clips; the candy-wrapper and volume-loss artifacts of linear blending
- **Collision detection and rigid-body dynamics**: broad phase by sweep-and-prune or bounding-volume hierarchies; narrow phase by GJK and separating-axis tests for convex shapes; contact manifolds; impulse-based resolution with restitution and friction; Newton's equations integrated at a fixed timestep, with tunnelling as the failure mode of large steps
- **Audio systems**: sample playback and mixing into a fixed-rate output buffer; the audio thread's real-time deadline and lock-free hand-off from the game thread; spatialization by distance attenuation, panning and Doppler; streaming of large assets and voice-count limits; latency as buffer size divided by sample rate
- **Input devices and game timing**: polling and event queues for keyboards, mice and gamepads; input latency measured from device to display; the high-resolution clock and frame timing; the fixed-timestep accumulator that runs zero or more simulation steps per rendered frame and interpolates state between them
- **Graphics pipeline**: vertex processing through model, view and projection transforms; primitive assembly, clipping, perspective division and viewport mapping; rasterization into fragments, the depth test and blending; the GPU as parallel stages; a frame as a sequence of draw calls and state changes
- **Shading and BRDFs**: the rendering equation; a bidirectional reflectance distribution function f(ωᵢ, ωₒ) and its energy conservation; Lambertian diffuse and Blinn–Phong specular; per-vertex versus per-pixel shading (Gouraud and Phong interpolation); the Cook–Torrance microfacet model with distribution, geometry and Fresnel terms
- **Texturing and mipmaps**: texture coordinates by barycentric interpolation; nearest, bilinear and trilinear filtering; mipmap chains costing about one third more memory; level of detail from the screen-space derivatives of texture coordinates; anisotropic filtering against blur at grazing angles
- **Shadow maps**: rendering depth from the light's view; comparing each fragment's light-space depth with the stored depth under a bias; shadow acne and peter-panning as the bias failure modes; percentage-closer filtering for soft edges; cascaded shadow maps splitting the view frustum to keep resolution near the camera
- **Physically based rendering**: energy-conserving BRDFs parameterized by albedo, metalness and roughness; the microfacet specular term; image-based lighting from a prefiltered environment map for diffuse and specular; the split-sum approximation for real-time specular; the linear-light pipeline in which textures and lighting are converted and combined before display
- **Global illumination**: indirect light as the recursive term of the rendering equation; light baking into lightmaps and probes; screen-space and voxel approximations; ambient occlusion as a visibility term; the cost of each approximation and its failures where information is missing, such as off-screen geometry
- **Image-space effects (tone mapping, depth of field, motion blur)**: tone mapping of high-dynamic-range radiance into display range with exposure and a curve such as Reinhard or an ACES-style filmic curve; depth of field from the circle of confusion computed from depth; motion blur from a per-pixel velocity buffer; the post-processing chain as full-screen passes and their bandwidth cost
- **Ray tracing and BVH acceleration**: ray–primitive intersection; bounding volume hierarchies built by median or surface-area-heuristic splits, traversed in about logarithmic time per ray; the slab test for axis-aligned boxes; hardware ray tracing with denoising for real-time use; the rasterization-versus-tracing trade-off
- **Level of detail and culling**: view-frustum culling against bounding volumes; occlusion culling with hierarchical depth buffers; backface culling; discrete LOD switching by distance with hysteresis and continuous LOD by geometry morphing; a screen-space error metric that decides when to switch
- **Virtual and augmented reality**: stereo rendering from two eye viewpoints with asymmetric projection frusta; the motion-to-photon latency budget, a commonly quoted target of about 20 ms to be checked against the headset vendor's figures, and time-warp reprojection to hide late frames; inside-out and outside-in tracking; passthrough and anchoring for augmented reality
- **Curves and splines**: parametric curves; Bézier curves evaluated by de Casteljau's algorithm; Catmull–Rom and cubic Hermite splines through control points; B-splines with local support over a knot vector; tangent continuity (C1) and curvature continuity (C2) at the joins; their use in paths, animation curves and surfaces

### Exercises

- From scratch: a software rasterizer that transforms triangles, clips them against the view frustum, rasterizes with edge functions, interpolates depth and barycentric attributes, and writes the frame to a PPM image checked against a known scene
- From scratch: a ray tracer with a bounding volume hierarchy built by a surface-area split, its ray-primitive test count compared against a brute-force loop over the same scene
- From scratch: an entity-component game loop with a fixed-timestep physics step, an accumulator and interpolated rendering, with particles colliding with boxes, and a test that replays a recorded input sequence to the same state
- **Reasoning drills**
  - Frame-budget arithmetic: at 60 frames per second a frame has about 16.7 ms; split that budget across input, simulation, culling, draw submission and GPU time, and predict which stage a given scene size breaks first
  - Choosing a culling strategy: for a scene of a given size and occluder density, choose between frustum culling alone, occlusion culling and a spatial index, and state the expected visible-object count before measuring
