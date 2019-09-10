<template>
    <div id="home">
        <!-- Hero-->
        <section class="hero is-large">
            <div class="hero-body">
                <div class="container">
                    <div class="columns is-vcentered" data-aos="fade-left">
                        <div class="column is-half has-text-right">
                            <figure class="image is-horizontal-center">
                                <img src="../assets/img/logo.png" alt="">
                            </figure>
                            <h2 class="subtitle">
                                Graditude is Job 1.
                            </h2>
                        </div>
                        <div class="column is-half">

                        </div>
                    </div>

                </div>
            </div>
        </section>
        <!-- End of Hero -->

        <!-- Communication -->
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-full has-text-centered" data-aos="fade-left">
                        <p class="is-size-2">Land your next job, starting now.</p>
                        <p>Are you a new graduate software engineer? Well, you've come to the right place.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="columns is-centered">
                    <div class="column is-one-third has-text-centered" data-aos="zoom-in">
                        <figure class="image is-128x128 is-horizontal-center">
                            <img src="../assets/img/database.svg" alt="">
                        </figure>
                        <p class="promo-caption">Searching, made simple</p>
                        <p class="light center">Graditude provides a simple, centralized database for new graduate
                            software engineers to land their next job. Curated using Indeed, our listings are updated
                            twice a day, every day.
                        </p>

                    </div>
                    <div class="column is-one-third has-text-centered" data-aos="zoom-in">
                        <figure class="image is-128x128 is-horizontal-center">
                            <img src="../assets/img/yoga.svg" alt="">
                        </figure>
                        <p class="promo-caption">Ad-free, stress-free.</p>
                        <p class="light center">Straight to the point, Graditude makes job-hunting stress-free by
                            filtering out ads and displaying posts in a tabular format. The less clicks made, the more efficient time is spent.</p>
                    </div>
                    <div class="column is-one-third has-text-centered" data-aos="zoom-in">
                        <figure class="image is-128x128 is-horizontal-center">
                            <img src="../assets/img/support.svg" alt="">
                        </figure>
                        <p class="promo-caption">Stay Motivated.</p>
                        <p class="light center">Job hunting for new graduates can be tough. Graditude's mission is to
                            encourage the growth of the next generation of professionals.
                        </p>
                    </div>
                </div>
            </div>

        </section>
        <section>
            <div class="container">
                <div class="columns is-centered" data-aos="fade-left">
                    <div class="column is-one-quarter has-text-centered">
                        <a href="" class="button is-info">Ready to elevate your search?</a>
                    </div>
                </div>

            </div>
        </section>
        <section class="section">
            <div class="container">
                <div class="column">
                    <JobsTable></JobsTable>
                </div>
            </div>

        </section>
        <!-- Footer -->
        <footer class="section">
            <hr>

            <div class="container">
                <div class="item columns" style="">
                    <div class="column is-full">
                        <nav class="level" style="">
                            <div class="level-item">
                                <p>Questions or Comments? <a href="">Contact us!</a></p>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>
    import JobsTable from '../components/JobsTable';

    export default {
        name: 'home',
        components: {
            JobsTable: JobsTable
        }

    }
</script>

<style>
    .is-horizontal-center {
        margin-left: auto;
        margin-right: auto;
    }
</style>
