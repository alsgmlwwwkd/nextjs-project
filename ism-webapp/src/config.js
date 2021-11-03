import awsExports from "./aws-exports";

export const awsConfig = {
    ...awsExports,
    API: {
        endpoints: [
            {
                name: "ism",
                region: "ap-northeast-2",
                endpoint: "https://xxnloez0hb.execute-api.ap-northeast-2.amazonaws.com/dev"
            }
        ]
    }
}