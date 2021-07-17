import groovy.json.JsonOutput
def copPipelineUtil = library('some-pipeline-step').com.library.path.here
def artifactoryCreds

properties([
    parameters([
        booleanParam(name: 'Release', defaultValue: false, description: "Enables non-master branch deployment"),
    ])
])

node {
    // this image comes (modified) from some repo
    def image = docker.image('<repo>/container/path:<tag>')

    stage('clean workspace') {
        sh 'ls -l && sudo rm -rf ./*'
        scmVariables = checkout([
            $class: 'GitSCM',
            branches: scm.branches,
            doGenerateSubmoduleConfigurations: scm.doGenerateSubmoduleConfigurations,
            extensions: [[$class: 'CloneOption', noTags: false, shallow: false, depth: 0, reference: '']],
            userRemoteConfigs: scm.userRemoteConfigs,
        ])
    }

    stage('get cerberus credentials') {
        artifactoryCreds = copPipelineUtil.Cerberus.new(this).safeDepositBox('somekindacreds', ['username', 'password'])
    }

    stage('test') {
        image.inside {
            sh """
            sed -i 's/unit_tests.py/*tests.py/g' pytest.ini
            pip install -r ./requirements.txt --user
            pip install -r ./requirements-dev.txt --user
            python ./setup.py pytest
            """
        }
    }

    stage('release') {
        if (env.BRANCH_NAME == 'master' || params.Release) {
            PATCH_VERSION = env.BRANCH_NAME == 'master' ? "${env.BUILD_NUMBER}" : "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

            image.inside {

                sh """
                pip install -r ./requirements.txt --user
                JENKINS_PATCH_VERSION=$PATCH_VERSION python3 setup.py bdist_egg bdist_wheel
                """

                artifactoryCreds.withCreds { secrets ->
                    sh """
                    twine upload \
                        --repository-url <repo>/container/path:<tag> \
                        --username ${secrets.username} \
                        --password ${secrets.password} \
                        dist/*.whl dist/*.egg
                    """
                }
            }

        } else {
            echo 'Deployment skipped: Executed for master branch builds only.'
        }
    }
}
